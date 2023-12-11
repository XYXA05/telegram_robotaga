import asyncio
import openai
from telethon.sync import TelegramClient, events, functions, types
from django.core.management.base import BaseCommand
from telethon.tl.functions.photos import UploadProfilePhotoRequest
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.sessions import StringSession
from rabstvo.models import TelegramUser, Channel, Potoci, Api_tocken
from rabstvo.classes import model_map
import telethon.errors
from telethon.errors import SessionPasswordNeededError





class Command(BaseCommand):
    help = 'botari'


    async def change_profile(self, client0, user_photo, name_first, name_last, bio_user):

        results = await client0(functions.photos.UploadProfilePhotoRequest(
            fallback=True,
            file=await client0.upload_file(user_photo.path)
            ))        

        #print(results.stringify()) 
        result = await client0(functions.account.UpdateProfileRequest(
            first_name=name_first,
            last_name=name_last,
            about=bio_user,
            ))
        #print(result)

    async def handle_client0(self, api, api_has, phone, link_kanals, model_choice, texts, user_photo, name_first, name_last, bio_user, time_answer, token, where_code_tg, password):

        client0 = TelegramClient(name_first, api, api_has)
        await client0.connect()
        if not await client0.is_user_authorized():
            code = input(f"{where_code_tg} - code:")
            await client0.send_code_request(phone)
            try:
                await client0.sign_in(phone=phone, code=code)
            except telethon.errors.SessionPasswordNeededError:
                await client0.sign_in(password=password)

        await self.change_profile(client0, user_photo, name_first, name_last, bio_user)

        for link in link_kanals:
            if not "https://t.me/" in link: 
                try:
                    invite = await client0(functions.messages.ImportChatInviteRequest(hash=link))
                    chat = invite.chats[0]
                    chat_entity = await client0.get_entity(chat)
                    print("Invite link has expired:", link)
                except Exception as e:
                    print(f"Error joining chat: {e}")
                    continue
            else:
                try:
                    open = await client0(functions.channels.JoinChannelRequest(channel=link))
                    opens = open.chats[0]
                    chat_entity = await client0.get_entity(opens)
                        #chat = chat_entity.id
                except Exception as e:
                    print(f"Error getting chat entity: {e}")
                    continue

            print(f"Current chat: {chat_entity.title}")


        @client0.on(events.NewMessage(outgoing=False))
        async def handle_new_message(event):

            chat_entity = event.chat
            if isinstance(chat_entity, types.Channel) and not chat_entity.megagroup:
                model_class = model_map[model_choice]
                if model_choice == "spintaxst":
                    t1 = model_class(texts)
                            
                if model_choice == "test1":
                            # Generate message using a prompt
                    t1 = model_class(f"{texts} : {event.message.message}")
                elif model_choice == "text_zagatovga":
                                # Generate message using pre-prepared text
                    t1 = model_class(texts)
                message = t1.get_response()
                            
                await asyncio.sleep(time_answer)
                await client0.send_message(event.chat, message, comment_to=event.id)
                    #message_sent = True  # Set the flag to True
        await client0.run_until_disconnected()





    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('all good'))
        

        telegram_user = TelegramUser.objects.all()
        tokehs = Api_tocken.objects.all()
        
        loop = asyncio.get_event_loop()
        tasks = []

        for user in telegram_user:
            print(f"Current user: {user}")
            api = user.api_id
            api_has = user.api_hash
            phone = user.phone
            name_first = user.name
            name_last = user.familia
            bio_user = user.bio
            user_photo = user.image
            where_code_tg = user.get_code
            password = user.password_2fa

            telegram_channel = Channel.objects.filter(boti__id=user.id)
            stile_answer = Potoci.objects.filter(user__id=user.id)

            link_kanals = [channel.process_links() for channel in telegram_channel][0]
            print(link_kanals)

            for stile_answers in stile_answer:
                print(f"stile answer: {stile_answers}")
                model_choice = stile_answers.paragraf_for_chat
                texts = stile_answers.text
                time_answer = stile_answers.time_stop
                
                for token_api in tokehs:
                    token = token_api.api_key
                    openai.api_key = token


                task = loop.create_task(self.handle_client0(api, api_has, phone, link_kanals, model_choice, texts, user_photo, name_first, name_last, bio_user, time_answer, token, where_code_tg, password))
                tasks.append(task)

        loop.run_until_complete(asyncio.wait(tasks))




















        #api = '24872411'
        #api_hash = 'd3352f1d4d12b68de0f74c1579afd3f1'
        #phone = '+380938563156'
        #kanali = ['https://t.me/desertigo']



        #api1 = '24952662'
        #api_hash1 = '8022f6be4af51fc66413ae5ea529cf7d'
        #phone1 = '+380666093575'
        #kanali1 = ['https://t.me/dedosigor']

        #stile_answer = Potoci.objects.filter(id = telegram_user)