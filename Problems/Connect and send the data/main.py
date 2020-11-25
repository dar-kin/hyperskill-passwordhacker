def submit_data(data, client, address):
    client.connect(address)
    msg = data.encode()
    client.send(msg)
    client.close()
