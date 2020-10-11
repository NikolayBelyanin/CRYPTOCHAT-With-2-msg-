import ast
import json
import rsa
import binascii
from Cryptodome.Signature import PKCS1_v1_5

#1 variant
def ENCRYPT_SENDER(Sender_public_key,msg):
    Message_b = msg.encode('utf-8')
    msg_from_sender = rsa.encrypt(Message_b, RSA.importKey(binascii.unhexlify(Sender_public_key)))
    return str(msg_from_sender)

def ENCRYPT_RECIPIENT(Recipient_public_key, msg):
    Message_b = msg.encode('utf-8')
    msg_to_recipient = rsa.encrypt(Message_b, Recipient_public_key)
    return  str(msg_to_recipient)

def get_msg_with_decrypt():
    with open('wallet-5000.txt', mode='r') as f:
        keys = f.readlines()
        public_key = keys[0][:-1]
        private_key = keys[1]
    with open('blockchain-5000.txt', 'r') as f:
        file_content = f.readlines()
        blockchain = json.loads(file_content[0][:-1])
        for block in blockchain[::-1]:
            for transactions in block['transactions']:
                if transactions['recipient'] == public_key:
                    msg_encrypt = transactions['msg_to(recipient)']
                    msg_decrypt = rsa.decrypt(ast.literal_eval(msg_encrypt), PKCS1_v1_5.new(RSA.importKey(binascii.unhexlify(wallet.private_key))))
                    return msg_decrypt.decode('utf-8')
                if transactions['sender'] == public_key:
                    msg_encrypt = transactions['msg_from(sender)']
                    msg_decrypt = rsa.decrypt(ast.literal_eval(msg_encrypt), PKCS1_v1_5.new(RSA.importKey(binascii.unhexlify(wallet.private_key))))
                    return msg_decrypt.decode('utf-8')


def get_msg_sender():
    with open('wallet-5000.txt', mode='r') as f:
        keys = f.readlines()
        public_key = keys[0][:-1]
    with open('blockchain-5000.txt', 'r') as f:
        file_content = f.readlines()
        blockchain = json.loads(file_content[0][:-1])
        for block in blockchain[::-1]:
            for transactions in block['transactions']:
                if transactions['sender'] == public_key:
                    return transactions['msg']

def get_msg_recipient():
    with open('wallet-5000.txt', mode='r') as f:
        keys = f.readlines()
        public_key = keys[0][:-1]
    with open('blockchain-5000.txt', 'r') as f:
        file_content = f.readlines()
        blockchain = json.loads(file_content[0][:-1])
        for block in blockchain[::-1]:
            for transactions in block['transactions']:
                if transactions['recipient'] == public_key:
                    return transactions['msg']

def DECRYPT_Sender(msg_decrypt):
    with open('wallet-5000.txt', mode='r') as f:
        keys = f.readlines()
        private_key = keys[1]
    msg = get_msg_sender()
    msg_decrypted = rsa.decrypt(ast.literal_eval(msg), PKCS1_v1_5.new(RSA.importKey(binascii.unhexlify(wallet.private_key))))
    return msg_decrypted

def DECRYPT_Recipient(msg_decrypt):
    with open('wallet-5000.txt', mode='r') as f:
        keys = f.readlines()
        private_key = keys[1]
    msg = get_msg_recipient()
    msg_decrypted = rsa.decrypt(ast.literal_eval(msg), PKCS1_v1_5.new(RSA.importKey(binascii.unhexlify(wallet.private_key))))
    return msg_decrypted