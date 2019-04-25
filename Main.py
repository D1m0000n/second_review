import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from random import randint


from vk_bot import VkBot


flag = None
identify = None


def write_msg(user_id, message):
    # vk.method('messages.send', {'user_id': user_id, 'message': message})
    random_id = randint(1, 100000)
    vk.method('messages.send', {
        'user_id': user_id,
        'message': message,
        'random_id': random_id
    })


token = "bc07c528f637a1fe3e9ed99ffbcae5928a512d09b0540b2228bca37b4966e918d55e5a712dad368a0e8c9"
vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)

print("Bot have been started")
for event in longpoll.listen():

    if event.type == VkEventType.MESSAGE_NEW:

        if event.to_me:

            print('New message:')
            print(f'For me by: {event.user_id}', end='')

            bot = VkBot(event.user_id)

            message, flag = bot.new_message(event.text, flag)
            write_msg(event.user_id, message)
            print('Text: ', event.text)

#необходимо писать название города на русском языке
#но существует защита от неправильного или несуществующего города
