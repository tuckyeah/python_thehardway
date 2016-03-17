import hashmap

sample = hashmap.new()
print "empty dict: "
print sample

hashmap.set(sample, "key1", "value1")
hashmap.set(sample, "key2", "value2")
hashmap.set(sample, "key3", "value3")
hashmap.set(sample, "apples", "bananas")

print "hash_key: "
print hashmap.hash_key(sample, "key1")
print hashmap.hash_key(sample, "key2")
print hashmap.hash_key(sample, "key3")
print hashmap.hash_key(sample, "apples")

print "get_bucket: "
print hashmap.get_bucket(sample, "key1")

print "get_slot: "
print hashmap.get_slot(sample, "key1")
print hashmap.get_slot(sample, "key2")
print hashmap.get_slot(sample, "key3")

print "dictionary again: "
print sample

print "list: "
print hashmap.list(sample)