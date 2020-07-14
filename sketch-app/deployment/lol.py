
import sys
import yaml
try:
	ver =sys.argv[1] 
except:
	pass

with open('sketchbackend-depl.yaml') as f:
  data = yaml.load(f,yaml.FullLoader)
image = data['spec']['template']['spec']['containers'][0]['image']
print("Initial Image -> ",image)
try:
	data['spec']['template']['spec']['containers'][0]['image'] = 'kumarnitesh2000/sketch_backend:'+ver
except:
	data['spec']['template']['spec']['containers'][0]['image'] = 'kumarnitesh2000/sketch_backend:latest'
with open('sketchbackend-depl.yaml','w') as f:
  data = yaml.dump(data,f)


with open('sketchbackend-depl.yaml') as f:
  data = yaml.load(f,yaml.FullLoader)
image = data['spec']['template']['spec']['containers'][0]['image']
print("Final Image -> ",image)
