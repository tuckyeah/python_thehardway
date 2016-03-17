"""
	the aMap is a list of buckets. 
	Each bucket is a list of slots.
	Each slot contains a (key/value) tuple/pair.
	the aMap looks like [[bucket][bucket][bucket][bucket][bucket][bucket][bucket][bucket][bucket][bucket][bucket]...]
	a bucket looks like [slot1, slot2...]
"""

def new(num_buckets=256):
	"""Initializes a Map with the given number of buckets."""
	#sets aMap variable to an empty list
	#then fills that list with the specified number of other empty lists ('buckets') 
	#returns the new aMap
	aMap = []
	for i in range(0, num_buckets):
		aMap.append([])
	return aMap

#this is the core of how a dict works!
def hash_key(aMap, key):
	"""Given a key, this will create a number and then convert it to
	an Index for the aMap's buckets."""
	#uses the hash function to get the unique integer associated with the key
	#then uses the modulus to make sure that number is in the range of the aMap
	return hash(key) % len(aMap)
	
def get_bucket(aMap, key):
	"""Given a key, find the bucket where it would go."""
	#uses the hash_key to give us a bucket where the key COULD be in
	#since it's possible that we'd get the same hash_key for two diff values
	bucket_id = hash_key(aMap, key)
	return aMap[bucket_id]
	
def get_slot(aMap, key, default=None):
	"""
	Returns the index, key, and value of a slot found in a bucket.
	Returns -1, key, and default (None if not set) when not found.
	"""
	#now that we know which bucket the key could be in
	#we iterate through all the elements of that bucket until it finds the key
	
	bucket = get_bucket(aMap, key)
	
	for i, kv in enumerate(bucket):
	#enumerate returns a tuple containing the count (starting at 0) 
	#and values obtained from iterating over the sequence
		k, v = kv
		#unpacks the elements in the bucket into 'key' and 'value'
		if key == k:
			return i, k, v 
	#if the slot does not contain the key, then it returns "none"
	return -1, key, default
	
def get(aMap, key, default=None):
	"""Gets the value in a bucket for the given key, or the default."""
	#assigns variables to the same values we received from the get_slot function
	#index of the slot, the key and the value it found.
	i, k, v = get_slot(aMap, key, default=default)
	#but all we care about is the value, so that's all we return
	#this is _basically_ the same thing as get_slot, but since most people
	#only care about the value from this kind of function, that's all we return
	return v 
	
def set(aMap, key, value):
	"""Sets the key to the value, replacing any existing value."""
	#finds the bucket the key could be in and sets it to bucket
	bucket = get_bucket(aMap, key)
	#sets the slot index, key and value from the get_slot function
	i, k, v = get_slot(aMap, key)
	
	#if the index is greater than zero, that means the key exists
	if i >= 0:
		#the key exists, replace it
		bucket[i] = (key, value)
	else:
		#because we return -1 if the key isn't found in get_slot, we know
		#the key does not, append to create it
		bucket.append((key, value))
		
def delete(aMap, key):
	"""Deletes the given key from the Map."""
	#get the bucket that they key is in, and sets it to bucket
	bucket = get_bucket(aMap, key)

	for i in xrange(len(bucket)):
		k, v = bucket[i]
		if key == k:
			del bucket[i]
			#we can break here, since we know there can be only one key/value pair
			break
			
def list(aMap):
	"""Prints out what's in the Map"""
	#iterates through every bucket in aMap
	for bucket in aMap:
		#if the bucket contains information...
		if bucket:
			#unpacks the key/value and prints
			for k, v in bucket:
				print k, v 

def dump(aMap):
	"""Dumps the full contents of every bucket so we can debug it"""
	for bucket in aMap:
		print bucket