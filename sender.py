import sys
import logging
import string
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

#check for a valid IP address
def validateIP(s):
	address=s.split('.')
	if len(address)!=4:
		return False
	for x in address:
		if not x.isdigit():
			return False
		i=int(x)
		if i<0 or i>255:
			return False
	return True
#end of validateIP

print 'Command-Line:', sys.argv
destination_ip=sys.argv[1];
interface=sys.argv[2]
type_of_protocol=sys.argv[3]

#trimming the message
message=''
for j in range(4, len(sys.argv)):
	message=message+sys.argv[j]+" "
message=message.strip()


#message=sys.argv[4:]
print 'Destination IP:',destination_ip
print 'Interface:',interface
print 'Type:', type_of_protocol
#print 'Message:', message[0], message[1]
print "Message:",message

#separate the message bytes and convert them to hex
if validateIP(destination_ip):
	if type_of_protocol in ('0','1','2'):		#check if the protocol is in the given range (0 or 1 or 2)
		
		#ICMP Message
		if (type_of_protocol=='0'):
			random_id=random.randint(0,255)
			random_id_in_hex="{:02x}".format(random_id)
			print random_id_in_hex
			print 'ICMP Echo Request Message'
			i=0
			for letter in message:
				each_letter="{:02x}".format(ord(letter))
				#print each_letter
				high=each_letter
				combine=high+random_id_in_hex
				value_in_id_field=int (combine,16)		#final id value
				#print value_in_id_field
				send (IP(id=value_in_id_field, frag=i, dst=destination_ip)/ICMP())	#send packet
				i=i+1
			#last packet		
			length_in_hex="{:02x}".format(i)
			if (i<256):
				length_in_hex='10'+length_in_hex
			else:
				length_in_hex='1'+length_in_hex			
			final_frag=int(length_in_hex,16)
			#print length_in_hex, final_frag
			high="{:02x}".format(0)
			final_combine_id=high+random_id_in_hex
			last_id_field=int (final_combine_id,16)
			send (IP(id=last_id_field, frag=final_frag, dst=destination_ip)/ICMP())		#send the last packet	
			#ICMP Message
		
		

		#TCP SYN Message		
		if (type_of_protocol=='1'):
			random_id=random.randint(0,255)
			random_id_in_hex="{:02x}".format(random_id)
			print random_id_in_hex
			print 'TCP SYN Packet'
			i=0
			for letter in message:
				each_letter="{:02x}".format(ord(letter))
				#print each_letter
				high=each_letter
				combine=high+random_id_in_hex
				value_in_id_field=int (combine,16)		#final id value
				#print value_in_id_field
				send (IP(id=value_in_id_field, frag=i, dst=destination_ip)/TCP(dport=80,flags="S"))	#send the packet
				i=i+1
			#last packet		
			length_in_hex="{:02x}".format(i)
			if (i<256):
				length_in_hex='10'+length_in_hex
			else:
				length_in_hex='1'+length_in_hex			
			final_frag=int(length_in_hex,16)
			#print length_in_hex, final_frag
			high="{:02x}".format(0)
			final_combine_id=high+random_id_in_hex
			last_id_field=int (final_combine_id,16)
			send (IP(id=last_id_field, frag=final_frag, dst=destination_ip)/TCP(dport=80,flags="S"))	#send the last packet


		

		#UDP Message
		if (type_of_protocol=='2'):
			random_id=random.randint(0,255)
			random_id_in_hex="{:02x}".format(random_id)
			print random_id_in_hex
			print 'UDP Packet'
			i=0
			for letter in message:
				each_letter="{:02x}".format(ord(letter))
				#print each_letter
				high=each_letter
				combine=high+random_id_in_hex
				value_in_id_field=int (combine,16)		#final id value
				#print value_in_id_field
				send (IP(id=value_in_id_field, frag=i, dst=destination_ip)/UDP(dport=53))	#send the packet
				i=i+1
			#last packet		
			length_in_hex="{:02x}".format(i)
			if (i<256):
				length_in_hex='10'+length_in_hex
			else:
				length_in_hex='1'+length_in_hex			
			final_frag=int(length_in_hex,16)
			#print length_in_hex, final_frag
			high="{:02x}".format(0)
			final_combine_id=high+random_id_in_hex
			last_id_field=int (final_combine_id,16)
			send (IP(id=last_id_field, frag=final_frag, dst=destination_ip)/UDP(dport=53))	#send the last packet


	else: print 'Invalid protocol'
else: print 'Invalid IP address'
