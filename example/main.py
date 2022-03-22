from src.utils import get_view_count, get_like_count, get_video_id

url = 'https://www.youtube.com/watch?v=kFRdoYfZYUY'
view_count = get_view_count(url)
print(f'Number of views: {view_count}')

like_count = get_like_count(url)
print(f'Number of like: {like_count}')

video_id = get_video_id(url)
print(f'Id of the video : {video_id}')
