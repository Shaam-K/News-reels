from unicodedata import category
from django.shortcuts import render
import urllib.request
import json
# Create your views here.

def home_page(request):

    if request.method == 'POST':
        country = request.POST['country']

        source_news = urllib.request.urlopen('https://newsapi.org/v2/top-headlines?country='+ country +'&language=en&pageSize=10&excludeDomains=Astrologyzone.com&apiKey=70b38b850cb94519b0ff9c459c9e2eba').read()


        news_load = json.loads(source_news)


        news_data_one = {
            'title-one': news_load['articles'][0]['title'],
            'image-one': news_load['articles'][0]['urlToImage'],
            'content-one': news_load['articles'][0]['content'],
            'link-one': news_load['articles'][0]['url']
        }
        
        news_data_two = {
            'title-two': news_load['articles'][1]['title'],
            'image-two': news_load['articles'][1]['urlToImage'],
            'content-two': news_load['articles'][1]['content'],
            'link-two': news_load['articles'][1]['url']
        }

        news_data_three = {
            'title-three': news_load['articles'][2]['title'],
            'image-three': news_load['articles'][2]['urlToImage'],
            'content-three': news_load['articles'][2]['content'],
            'link-three': news_load['articles'][2]['url']
        }

        news_data_four = {
            'title-four': news_load['articles'][3]['title'],
            'image-four': news_load['articles'][3]['urlToImage'],
            'content-four': news_load['articles'][3]['content'],
            'link-four': news_load['articles'][3]['url']
        }

        news_data_five = {
            'title-five': news_load['articles'][4]['title'],
            'image-five': news_load['articles'][4]['urlToImage'],
            'content-five': news_load['articles'][4]['content'],
            'link-five': news_load['articles'][4]['url']
        }

        news_data_six = {
            'title-six': news_load['articles'][5]['title'],
            'image-six': news_load['articles'][5]['urlToImage'],
            'content-six': news_load['articles'][5]['content'],
            'link-six': news_load['articles'][5]['url']
        }

        news_data_seven = {
            'title-seven': news_load['articles'][6]['title'],
            'image-seven': news_load['articles'][6]['urlToImage'],
            'content-seven': news_load['articles'][6]['content'],
            'link-seven': news_load['articles'][6]['url']
        }

        news_data_eight = {
            'title-eight': news_load['articles'][7]['title'],
            'image-eight': news_load['articles'][7]['urlToImage'],
            'content-eight': news_load['articles'][7]['content'],
            'link-eight': news_load['articles'][7]['url']
        }

        news_data_nine = {
            'title-nine': news_load['articles'][8]['title'],
            'image-nine': news_load['articles'][8]['urlToImage'],
            'content-nine': news_load['articles'][8]['content'],
            'link-nine': news_load['articles'][8]['url']
        }

        news_data_ten = {
            'title-ten': news_load['articles'][9]['title'],
            'image-ten': news_load['articles'][9]['urlToImage'],
            'content-ten': news_load['articles'][9]['content'],
            'link-ten': news_load['articles'][9]['url']
        }



        title_one = news_data_one['title-one']
        image_one = news_data_one['image-one']
        content_one = news_data_one['content-one']
        link_one = news_data_one['link-one']
        title_two = news_data_two['title-two']
        image_two = news_data_two['image-two']
        content_two = news_data_two['content-two']
        link_two = news_data_two['link-two']
        title_three = news_data_three['title-three']
        image_three = news_data_three['image-three']
        content_three = news_data_three['content-three']
        link_three = news_data_three['link-three']
        title_four = news_data_four['title-four']
        image_four = news_data_four['image-four']
        content_four = news_data_four['content-four']
        link_four = news_data_four['link-four']
        title_five = news_data_five['title-five']
        image_five = news_data_five['image-five']
        content_five = news_data_five['content-five']
        link_five = news_data_five['link-five']
        title_six = news_data_six['title-six']
        image_six = news_data_six['image-six']
        content_six = news_data_six['content-six']
        link_six = news_data_six['link-six']
        title_seven = news_data_seven['title-seven']
        image_seven = news_data_seven['image-seven']
        content_seven = news_data_seven['content-seven']
        link_seven = news_data_seven['link-seven']
        title_eight = news_data_eight['title-eight']
        image_eight = news_data_eight['image-eight']
        content_eight = news_data_eight['content-eight']
        link_eight = news_data_eight['link-eight']
        title_nine = news_data_nine['title-nine']
        image_nine = news_data_nine['image-nine']
        content_nine = news_data_nine['content-nine']
        link_nine = news_data_nine['link-nine']
        title_ten = news_data_ten['title-ten']
        image_ten = news_data_ten['image-ten']
        content_ten = news_data_ten['content-ten']
        link_ten = news_data_ten['link-ten']

        intermediate_data = {
            'one_title': title_one,
            'one_image': image_one,
            'one_content': content_one,
            'one_link': link_one,
            'two_title': title_two,
            'two_image': image_two,
            'two_content': content_two,
            'two_link': link_two,
            'three_title': title_three,
            'three_image': image_three,
            'three_content': content_three,
            'three_link': link_four,
            'four_title': title_four,
            'four_image': image_four,
            'four_content': content_four,
            'four_link': link_four,
            'five_title': title_five,
            'five_image': image_five,
            'five_content': content_five,
            'five_link': link_five,
            'six_title': title_six,
            'six_image': image_six,
            'six_content': content_six,
            'six_link': link_six,
            'seven_title': title_seven,
            'seven_image': image_seven,
            'seven_content': content_seven,
            'seven_link': link_seven,
            'eight_title': title_eight,
            'eight_image': image_eight,
            'eight_content': content_eight,
            'eight_link': link_eight,
            'nine_title': title_nine,
            'nine_image': image_nine,
            'nine_content': content_nine,
            'nine_link': link_nine,
            'ten_title': title_ten,
            'ten_image': image_ten,
            'ten_content': content_ten,
            'ten_link': link_ten,
        }

        final_data = []
        final_data.append(intermediate_data)

        context = {'news' : final_data}
    
    else:
        context= {}
    return render(request, "home.html",context)



