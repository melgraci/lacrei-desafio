from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from .models import Consulta, Profissional


class ProfissionalAPITestCase(APITestCase):

    def setUp(self):
        self.url = '/api/profissionais/'

        self.usuario = User.objects.create_user(
            username='teste',
            password='senha-teste-123'
        )

        self.token = Token.objects.create(
            user=self.usuario
        )

        self.client.credentials(
            HTTP_AUTHORIZATION=f'Token {self.token.key}'
        )

        self.dados_profissional = {
            'nome_social': 'Maria Souza',
            'profissao': 'Nutricionista',
            'endereco': 'Machado - MG',
            'contato': '35988888888'
        }

    def test_criar_profissional(self):
        response = self.client.post(
            self.url,
            self.dados_profissional,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.data['nome_social'],
            'Maria Souza'
        )

        self.assertEqual(
            Profissional.objects.count(),
            1
        )

    def test_criar_profissional_sem_nome(self):
        dados_invalidos = {
            'nome_social': '',
            'profissao': 'Nutricionista',
            'endereco': 'Machado - MG',
            'contato': '35988888888'
        }

        response = self.client.post(
            self.url,
            dados_invalidos,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertEqual(
            Profissional.objects.count(),
            0
        )

    def test_atualizar_profissional(self):
        profissional = Profissional.objects.create(
            nome_social='Carlos Souza',
            profissao='Médico',
            endereco='Machado - MG',
            contato='35986666666'
        )

        dados_atualizados = {
            'nome_social': 'Carlos Oliveira',
            'profissao': 'Médico',
            'endereco': 'Poços de Caldas - MG',
            'contato': '35985555555'
        }

        response = self.client.put(
            f'/api/profissionais/{profissional.id}/',
            dados_atualizados,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.data['nome_social'],
            'Carlos Oliveira'
        )

    def test_excluir_profissional(self):
        profissional = Profissional.objects.create(
            nome_social='Ana Souza',
            profissao='Psicóloga',
            endereco='Machado - MG',
            contato='35984444444'
        )

        response = self.client.delete(
            f'/api/profissionais/{profissional.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertFalse(
            Profissional.objects.filter(
                id=profissional.id
            ).exists()
        )


class ConsultaAPITestCase(APITestCase):

    def setUp(self):
        self.url = '/api/consultas/'

        self.usuario = User.objects.create_user(
            username='teste_consulta',
            password='senha-teste-123'
        )

        self.token = Token.objects.create(
            user=self.usuario
        )

        self.client.credentials(
            HTTP_AUTHORIZATION=f'Token {self.token.key}'
        )

        self.profissional = Profissional.objects.create(
            nome_social='João Silva',
            profissao='Fisioterapeuta',
            endereco='Machado - MG',
            contato='35987777777'
        )

    def test_criar_consulta(self):
        dados_consulta = {
            'data': '2026-10-10T14:00:00Z',
            'profissional': self.profissional.id
        }

        response = self.client.post(
            self.url,
            dados_consulta,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.data['profissional'],
            self.profissional.id
        )

        self.assertEqual(
            Consulta.objects.count(),
            1
        )
    def test_atualizar_consulta(self):
        consulta = Consulta.objects.create(
            data='2026-10-10T14:00:00Z',
            profissional=self.profissional
        )

        dados_atualizados = {
            'data': '2026-10-15T16:00:00Z',
            'profissional': self.profissional.id
        }

        response = self.client.put(
            f'/api/consultas/{consulta.id}/',
            dados_atualizados,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.data['profissional'],
            self.profissional.id
        )

    def test_excluir_consulta(self):
        consulta = Consulta.objects.create(
            data='2026-10-10T14:00:00Z',
            profissional=self.profissional
        )

        response = self.client.delete(
            f'/api/consultas/{consulta.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertFalse(
            Consulta.objects.filter(
                id=consulta.id
            ).exists()
        )

    def test_filtrar_consultas_por_profissional(self):
        Consulta.objects.create(
            data='2026-10-10T14:00:00Z',
            profissional=self.profissional
        )

        response = self.client.get(
            self.url,
            {'profissional_id': self.profissional.id}
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            len(response.data),
            1
        )

        self.assertEqual(
            response.data[0]['profissional'],
            self.profissional.id
        )

    def test_criar_consulta_sem_data(self):
        dados_invalidos = {
            'profissional': self.profissional.id
        }

        response = self.client.post(
            self.url,
            dados_invalidos,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertEqual(
            Consulta.objects.count(),
            0
        )

    def test_criar_consulta_sem_profissional(self):
        dados_invalidos = {
            'data': '2026-10-10T14:00:00Z'
        }

        response = self.client.post(
            self.url,
            dados_invalidos,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertEqual(
            Consulta.objects.count(),
            0
        )

    def test_criar_consulta_profissional_inexistente(self):
        dados_invalidos = {
            'data': '2026-10-10T14:00:00Z',
            'profissional': 9999
        }

        response = self.client.post(
            self.url,
            dados_invalidos,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertEqual(
            Consulta.objects.count(),
            0
        )

class AuthenticationAPITestCase(APITestCase):

    def test_acesso_sem_token(self):
        response = self.client.get('/api/profissionais/')

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED
        )