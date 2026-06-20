from google import genai

from django.conf import settings
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

client = genai.Client(api_key=settings.GEMINI_API_KEY)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def ask_coach(request):
    question = request.data.get("question", "").strip()

    if not question:
        return Response(
            {"reply": "Please ask a question first."},
            status=400,
        )

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"""
You are PassPilot AI Coach.

You help learner drivers prepare for:

- UK Theory Test
- Road Signs
- Hazard Perception
- Practical Driving Test
- Roundabouts
- Motorways
- Parking
- Manoeuvres
- Vehicle Safety

You can answer general questions too.

Always explain clearly and encourage safe driving.

User question:

{question}
"""
        )

        return Response({
            "reply": response.text
        })

    except Exception as e:
        print("Gemini error:", e)

        return Response(
            {
                "reply": "Sorry, I couldn't connect to the AI coach right now."
            },
            status=500
        )