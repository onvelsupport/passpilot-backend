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

You can answer general questions too, but keep answers clear and practical.

Rules:
- Prioritise UK driving rules.
- Explain in simple language.
- Encourage safe driving.
- Do not give dangerous, illegal, or unsafe driving advice.

User question:
{question}
"""
        )

        return Response({"reply": response.text})

    except Exception as e:
        print("Gemini ask_coach error:", e)

        return Response(
            {"reply": "Sorry, I couldn't connect to the AI coach right now."},
            status=500,
        )


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def study_recommendation(request):
    weakest_topic = request.data.get("weakest_topic", "Not enough data")
    average_score = request.data.get("average_score", 0)
    current_streak = request.data.get("current_streak", 0)

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"""
You are PassPilot AI Coach.

The learner driver has:
Average score: {average_score}%
Current streak: {current_streak} days
Weakest topic: {weakest_topic}

Create a short personalised revision plan.

Format it like this:

Encouragement:
...

Weakest Topic:
...

Today's Revision Plan:
- ...
- ...
- ...

Estimated Study Time:
...

Keep it concise, friendly, and focused on UK theory test preparation.
"""
        )

        return Response({"reply": response.text})

    except Exception as e:
        print("Gemini study_recommendation error:", e)

        return Response(
            {"reply": "Unable to generate study recommendations."},
            status=500,
        )


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def explain_wrong_answer(request):
    question = request.data.get("question", "").strip()
    correct_answer = request.data.get("correct_answer", "").strip()
    user_answer = request.data.get("user_answer", "").strip()
    explanation = request.data.get("explanation", "").strip()

    if not question or not correct_answer:
        return Response(
            {"reply": "Question and correct answer are required."},
            status=400,
        )

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"""
You are PassPilot AI Coach.

Explain this UK driving theory question clearly.

Question:
{question}

User answer:
{user_answer}

Correct answer:
{correct_answer}

Existing explanation:
{explanation}

Explain:
1. Why the correct answer is right.
2. Why the user's answer may be wrong.
3. One practical driving tip.

Keep it simple and helpful.
"""
        )

        return Response({"reply": response.text})

    except Exception as e:
        print("Gemini explain_wrong_answer error:", e)

        return Response(
            {"reply": "Unable to explain this answer right now."},
            status=500,
        )


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def generate_similar_questions(request):
    topic = request.data.get("topic", "").strip()
    original_question = request.data.get("question", "").strip()

    if not topic and not original_question:
        return Response(
            {"reply": "Topic or question is required."},
            status=400,
        )

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"""
You are PassPilot AI Coach.

Generate 3 similar UK driving theory practice questions.

Topic:
{topic}

Original question:
{original_question}

For each question, include:
- question
- 4 options
- correct answer
- short explanation

Keep the questions realistic and suitable for learner drivers in Great Britain.
"""
        )

        return Response({"reply": response.text})

    except Exception as e:
        print("Gemini generate_similar_questions error:", e)

        return Response(
            {"reply": "Unable to generate similar questions right now."},
            status=500,
        )


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def examiner_mode(request):
    message = request.data.get("message", "").strip()

    if not message:
        return Response(
            {"reply": "Please enter a driving situation or response."},
            status=400,
        )

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"""
You are a calm UK practical driving test examiner.

Respond to the learner's message as if you are conducting a practical driving lesson or mock test.

Learner message:
{message}

Give clear, realistic driving examiner feedback.
Mention observations, control, positioning, mirrors, signalling, and safety where relevant.
Keep it concise.
"""
        )

        return Response({"reply": response.text})

    except Exception as e:
        print("Gemini examiner_mode error:", e)

        return Response(
            {"reply": "Unable to start examiner mode right now."},
            status=500,
        )