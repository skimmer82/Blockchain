#encoding utf-8
import hashlib
import json
import socket

f_in = open("input.txt","w")
f_out = open("ouput.txt","w")
for i in range(0,200000):
    load_f = open('block_head.json','r')
    load_dict = json.load(load_f)
    print load_dict[i]
    print "-------------"
    #version =  '0'+hex(socket.ntohl(load_dict[i]['version']))[2:-1]
    version = '{:08X}'.format(load_dict[i]['version']).decode('hex')[::-1].encode('hex')
    hash_prev_block =  (load_dict[i]['previousblockhash']).decode('hex')[::-1].encode('hex')
    hash_merkle_root =  (load_dict[i]['merkleroot']).decode('hex')[::-1].encode('hex')
    time = '{:08X}'.format(load_dict[i]['time']).decode('hex')[::-1].encode('hex')
    bits =  (load_dict[i]['bits']).decode('hex')[::-1].encode('hex')
    nonce = '{:08X}'.format(load_dict[i]['nonce']).decode('hex')[::-1].encode('hex')
    print version
    print hash_prev_block
    print hash_merkle_root
    print time
    print bits
    print '{:08X}'.format(load_dict[i]['nonce']).decode('hex')[::-1].encode('hex')

    header_hex = version+hash_prev_block+hash_merkle_root+time+bits+nonce
    header_hex_2 = version+hash_prev_block+hash_merkle_root+time+bits
#    print header_hex
#    print len(header_hex), len(header_hex_2)
    print >>f_in,'{:0608b}'.format(int(header_hex_2,16))
    print >>f_out,'{:032b}'.format(int(nonce,16))
#    header_bin = header_hex.decode('hex')
    #hash = hashlib.sha256(hashlib.sha256(header_bin).digest()).digest()
    #print hash.encode('hex_codec')
    #print hash[::-1].encode('hex_codec')
f_in.close()
f_out.close()
