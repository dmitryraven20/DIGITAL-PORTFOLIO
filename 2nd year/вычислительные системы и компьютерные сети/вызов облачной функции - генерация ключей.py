def handler(event,q):
    p = event['queryStringParameters']['p']
    q = event['queryStringParameters']['q']

    n = p * q
    phi = (p-1) * (q-1)
    
    e = 3

    k = 2
    d = ((k*phi)+1)//e

    pub = (e,n)
    priv = (d,n)

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'isBase64Encoded': False,
        'body': ('Pub keys: {}'.format(pub), 'Priv keys: {}'.format(priv))
    }
    