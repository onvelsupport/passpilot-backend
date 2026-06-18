from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class CoachView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        message = request.data.get('message', '').lower()

        if 'roundabout' in message:
            reply = (
                "Approach slowly, choose the correct lane early, "
                "give way to traffic from the right and signal before exiting."
            )

        elif 'road sign' in message or 'sign' in message:
            reply = (
                "Red circles give orders, triangles give warnings "
                "and blue signs usually provide instructions."
            )

        elif 'hazard' in message:
            reply = (
                "A hazard is anything that could make you change speed or direction."
            )

        elif 'fail' in message or 'practical test' in message:
            reply = (
                "Common reasons for failing include poor observation, "
                "incorrect mirror checks and bad lane discipline."
            )

        else:
            reply = (
                "I can help with theory questions, road signs, "
                "hazard perception and practical test preparation."
            )

        return Response({
            'reply': reply
        })