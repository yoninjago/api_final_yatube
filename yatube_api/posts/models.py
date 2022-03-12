from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    slug = models.SlugField(unique=True, verbose_name='Идентификатор')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(verbose_name='Содержание')
    pub_date = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата публикации')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор')
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True, verbose_name='Изображение')
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL,
        related_name="posts", blank=True, null=True, verbose_name='Группа')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    STR_METOD_TEMPLATE = (
        'Пост: {text:.15}... '
        'Дата публикации: {date:%d %b %Y}. '
        'Автор: {author}. '
        'Группа: {group}. ')

    def __str__(self):
        return self.STR_METOD_TEMPLATE.format(
            text=self.text,
            date=self.pub_date,
            author=self.author.username,
            group=self.group)


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор')
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Пост')
    text = models.TextField(verbose_name='Текст комментария')
    created = models.DateTimeField(
        auto_now_add=True, db_index=True, verbose_name='Дата добавления')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text[:15]


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик')
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор')

    class Meta:
        models.UniqueConstraint(
            fields=['following', 'user'], name='unique_follow')
        verbose_name = 'Подписка на авторов'
        verbose_name_plural = 'Подписки на авторов'

    def __str__(self):
        return (f'Подписка пользователя {self.user.username} '
                f'на автора {self.following.username}')
