import json

# {
# 	"seed-soil": [
# 		[
# 			50,
# 			98,
# 			2
# 		],
# 		[
# 			52,
# 			50,
# 			48
# 		]
# 	]
# }
with open('advent5.txt') as f:
	maps = ['seed-to-soil','soil-to-fertilizer','fertilizer-to-water','water-to-light','light-to-temperature','temperature-to-humidity','humidity-to-location']

	seeds = [int(x) for x in f.readline().split(':')[-1].strip().split(' ') if x != '']
	print(seeds)

	mapping_dict = {
		'seeds':seeds
	}

	active_map = ''
	for line in f.readlines():
		if active_map == '':
			if line.split(' ')[0] in maps:
				active_map = line.split(' ')[0].strip()
				print(active_map)
		else:
			if line.strip() == '':
				active_map = ''
			else:
				if active_map not in mapping_dict:
					mapping_dict[active_map] = []
				mapping_dict[active_map].append([int(x) for x in line.strip().split(' ') if x != ''])
	print(mapping_dict)


	# save to json
	with open('advent5_input.json','w') as json_file:
		json.dump(mapping_dict,json_file)

# for map in list(mapping_dict.keys())[1:]:
# 	# insert a 0,0 at the beginning
# 	# the 3rd value should be the same as the 2nd value
# 	# if there isn't a 0 in column 1:
# 	if mapping_dict[map][0][0] != 0:
# 		mapping_dict[map].insert(0,[0,0,mapping_dict[map][0][1]])
# 	mapping_dict[map].insert(0,[0,0,mapping_dict[map][0][0]])

# print(mapping_dict)

def forwards(map,number):
	# while number > map[i+1][0] and i+1 < len(map) - 1:
	# 	i += 1
	# dist = number - map[i][0]
	# val = map[i][1] + dist

	# find the range this fits into
	for i in range(len(map)):
		if number >= map[i][1] and number < map[i][1] + map[i][2]:
			# print(map[i],number,val,i)
			return map[i][0] + (number - map[i][1])
	# if still here, then it's just 0 (implicit)
	# print('zeroed',number)
	return number

loc_vals = []
for seed in mapping_dict['seeds']:
	val = seed
	for map in list(mapping_dict.keys())[1:]:
		print(map,val,end=': ')
		val = forwards(mapping_dict[map],val)
	loc_vals.append(val)
	print(loc_vals)

print(min(loc_vals))


# Part 2
# This is currently extremely inefficient and naive
# Need to refactor to use entire subranges of seeds rather than individual seeds
loc_vals = []
seeds_considered = 0
for si in range(0,len(mapping_dict['seeds']),2):
	seed_start,seed_len = mapping_dict['seeds'][si:si+2]
	for seed in range(seed_start,seed_start+seed_len):
		seeds_considered += 1
		val = seed
		for map in list(mapping_dict.keys())[1:]:
			# print(map,val,end=': ')
			val = forwards(mapping_dict[map],val)
		loc_vals.append(val)

print(min(loc_vals))