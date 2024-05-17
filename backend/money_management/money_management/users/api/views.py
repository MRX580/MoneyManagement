from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.mixins import UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import api_view

from money_management.users.models import User

from .serializers import UserSerializer


class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "pk"

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(id=self.request.user.id)

    @action(detail=False)
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)

@api_view(['GET'])
def get_data(request):
    data = {
        'totalAmount': {'value': 10000, 'change': '+20%'},
        'appleStock': {'value': 346, 'change': '+33%'},
        'btcPrice': {'value': 61524, 'change': '-8%'},
        'topExpenses': [
            {'category': 'Авто', 'amount': 2000},
            {'category': 'Дом', 'amount': 1100},
            {'category': 'Кафе и рестораны', 'amount': 1000},
            {'category': 'Такси', 'amount': 200},
        ],
        'transactions': [
            {'category': 'Кафе и рестораны', 'balance': 5700, 'amount': 1000, 'percentage': '-10%'},
            {'category': 'Такси', 'balance': 6700, 'amount': 200, 'percentage': '-2%'},
            {'category': 'Дом', 'balance': 6900, 'amount': 1100, 'percentage': '-11%'},
            {'category': 'Авто', 'balance': 8000, 'amount': 2000, 'percentage': '-20%'},
            {'category': 'Зарплата', 'balance': 10000, 'amount': 10000, 'percentage': '+'},
        ],
        'expenseAnalytics': [
            {'month': 'Jan', 'amount': 30000},
            {'month': 'Feb', 'amount': 40000},
            {'month': 'Mar', 'amount': 35000},
            {'month': 'Apr', 'amount': 45000},
            {'month': 'May', 'amount': 50000},
            {'month': 'Jun', 'amount': 55000},
            {'month': 'Jul', 'amount': 60000},
            {'month': 'Aug', 'amount': 65000},
            {'month': 'Sep', 'amount': 70000},
            {'month': 'Oct', 'amount': 75000},
            {'month': 'Nov', 'amount': 80000},
            {'month': 'Dec', 'amount': 85000},
        ]
    }
    return Response(data)