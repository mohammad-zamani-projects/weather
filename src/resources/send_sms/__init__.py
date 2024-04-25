import kavenegar

from weather.src import helpers


def send_message(message=None):
    try:
        api = kavenegar.KavenegarAPI(helpers.KAVENEGAR_API_KEY)
        params = {
            'sender': '10004346',
            'receptor': helpers.NUMBER_OF_SMS_RECEIVER,
            'message': message
        }
        response = api.sms_send(params)
        print(str(response))

    except kavenegar.APIException as e:
        print(str(e))
    except kavenegar.HTTPException as e:
        print(str(e))

