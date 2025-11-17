from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        api_key = request.headers.get('X-API-KEY')

        # API KEY 없으면 DRF 기본 인증(JWT 등)에 넘김
        if not api_key:
            return None  

        # KEY 값이 틀리면 인증 실패
        if api_key != "MY_SECRET_KEY_123":
            raise AuthenticationFailed('Invalid API Key')

        # 테스트용 사용자 자동 생성 또는 가져오기
        user, created = User.objects.get_or_create(
            username='test_api_user',
            defaults={'password': 'temporary1234!'}
        )

        return (user, None)