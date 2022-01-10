from django.shortcuts import render
from django.shortcuts import (
    get_object_or_404,
    render
)
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import (
    generics,
    mixins
)
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from .models import (
    Banks,
    Student
)
from .serializer import (
    BanksSerializer2,
    UserSerializer,
    StudentSerializer,
    StudentSerializer1,
    StudentSerializer2
)


# @api_view(http_method_names=['GET', 'POST'])
# def some_function(request):
#     print(request.method)
#     return Response({})

@api_view(http_method_names=['GET', 'POST'])
def some_function(request):
    if request.method == 'GET':
        bank = Banks.objects.all()
        serializer = BanksSerializer2(bank, many=True)
        return Response(data=serializer.data)

    elif request.method == 'POST':
        serializer = BanksSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'request': serializer.data})
        else:
            return Response({'request': 'Your data is not valid'})
        # return Response({'answer': 'This is POST Method'})


# @api_view(http_method_names=['GET', 'PUT', 'DELETE'])
# def sample_view(request, id: int):
#     if request.method == 'GET':
#         bank = Banks.objects.get(id=id)
#         serializer = BanksSerializer2(bank)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = BanksSerializer2(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response({'answer': 'This is PUT Method'})
#
#     elif request.method == 'DELETE':
#         bank = Banks.objects.get(id=id)
#         bank.delete()
#     return Response({'answer': 'This is DELETE Method'})


@api_view(http_method_names=['GET', 'PUT', 'DELETE'])
def sample_view(request, id: int):
    if request.method == 'GET':
        bank = get_object_or_404(Banks, id=id)
        serializer = BanksSerializer2(bank)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        bank = get_object_or_404(Banks, id=id)
        serializer = BanksSerializer2(bank, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({'answer': 'This is PUT Method'},
                        status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        bank = get_object_or_404(Banks, id=id)
        bank.delete()
        return Response({'request': "Your data is deleted"},
                        status=status.HTTP_200_OK)
    return Response({'requst': "Your data is not deleted"},
                    status=status.HTTP_400_BAD_REQUEST)

    # elif request.method == 'DELETE':
    #     bank = Banks.objects.get(id=id)
    #     bank.delete()
    # return Response({'answer': 'This is DELETE Method'})


class BanksDetails(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

    def get(self, request):
        bank = Banks.objects.all()
        serializer = BanksSerializer2(bank, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BanksSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'request': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class BankInfo(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

    def get(self, request, pk):
        bank = get_object_or_404(Banks, pk=pk)
        serializer = BanksSerializer2(bank)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        bank = get_object_or_404(Banks, pk=pk)
        serializer = BanksSerializer2(bank, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'request': "your data is updated"},
                            status=status.HTTP_200_OK)
        return Response({'request': "your data is not updated"},
                        status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        bank = get_object_or_404(Banks, pk=pk)
        try:
            bank.delete()
            data = {
                'request': "Data successfuly deleted"
            }
            return Response(data=data, status=status.HTTP_204_NO_CONTENT)
        except Exception:
            data = {

                'request': "Uuuh blya, code ne rabotaet"
            }
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


class BanksViewSet(viewsets.ViewSet):

    def list(self, request):
        bank = Banks.objects.all()
        serializer = BanksSerializer2(bank, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = BanksSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        bank = get_object_or_404(Banks, pk=pk)
        serializer = BanksSerializer2(bank)
        return Response(serializer.data)

    def update(self, request, pk):
        bank = get_object_or_404(Banks, pk=pk)
        serializer = BanksSerializer2(bank, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'request': "your data is updated"},
                            status=status.HTTP_200_OK)
        return Response({'request': "your data is not updated"},
                        status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        bank = get_object_or_404(Banks, pk=pk)
        try:
            bank.delete()
            data = {
                'request': "Data successfuly deleted"
            }
            return Response(data=data, status=status.HTTP_204_NO_CONTENT)
        except Exception:
            data = {

                'request': "Uuuh blya, code ne rabotaet"
            }
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


class BanksList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Banks.objects.all()
    serializer_class = BanksSerializer2

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BanksDetail(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    queryset = Banks.objects.all()
    serializer_class = BanksSerializer2

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class BanksListGenerics(generics.ListCreateAPIView):
    queryset = Banks.objects.all()
    serializer_class = BanksSerializer2


class BanksDetailGenerics(generics.RetrieveUpdateDestroyAPIView):
    queryset = Banks.objects.all()
    serializer_class = BanksSerializer2


# 7 January 2022 year

class LoginView(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username
        }, status=status.HTTP_201_CREATED)


class Logout(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

    def get(self, requset, format=None):
        requset.user.auth_token.delete()
        return Response({'response': 'token deleted'}, status=status.HTTP_200_OK)


class SignUp(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#  08/01/2022  #


class StudentListGenerics(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetailGenerics(generics.RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# 10.01.2022 #

class StudentDetails(APIView):

    def get(self, requst):
        student = Student.objects.all()
        serializer = StudentSerializer1(student, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, requst):
        serializer = StudentSerializer2(data=requst.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"request": "Your data is updated"}, status=status.HTTP_200_OK)
        else:
            return Response({"request": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        student = get_object_or_404(Student, id=id)
        student.delete()
        return Response({"request": "Your data is deleted"}, status=status.HTTP_200_OK)