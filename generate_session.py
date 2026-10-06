from telethon.sync import TelegramClient
from telethon.sessions import StringSession

print("=" * 60)
print("Telegram SESSION_STRING 生成器")
print("=" * 60)

api_id = int(input("请输入 API_ID: ").strip())
api_hash = input("请输入 API_HASH: ").strip()

with TelegramClient(
    StringSession(),
    api_id,
    api_hash
) as client:

    print("\n正在连接 Telegram...")

    print("\n如果 Telegram 要求验证码，请输入 Telegram 收到的验证码。")
    print("如果开启了两步验证，还会要求输入 2FA 密码。\n")

    session = client.session.save()

    print("\n" + "=" * 60)
    print("SESSION_STRING:")
    print("=" * 60)

    print(session)

    print("=" * 60)
    print("\nSESSION_STRING 生成完成。")
