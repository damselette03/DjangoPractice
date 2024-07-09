from django.contrib.auth.models import User

# 创建一个新用户
user = User.objects.create_user(username='testuser', password='testpassword')

# 如果需要设置邮箱
user.email = 'testuser@example.com'
user.save()
