text = 'She sells sea shells on the sea shore The shells that she sells are sea shells I\'m sure.So if she sells ' \
       'seashells on the sea shore I\'m sure that the shells are sea shore shells'.lower()
d = {i for i in text.split(' ')}
print(d, len(d))
