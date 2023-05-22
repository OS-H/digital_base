'''
text demo
'''

from elasticsearch import Elasticsearch

# connect Elasticsearch node
es = Elasticsearch(['localhost:9200'])

# new index and put one content
doc = {
    'title': 'Python Elasticsearch demo',
    'content': 'this is a Python Elasticsearch content',
    'tags': ['Python', 'Elasticsearch']
}
res = es.index(index='my_index', id=1, body=doc)
print(res['result'])

# get data from index
res = es.get(index='my_index', id=1)
print(res['_source'])

# query contain "Python" content
query = {
    'query': {
        'match': {
            'content': 'Python'
        }
    }
}
res = es.search(index='my_index', body=query)
for hit in res['hits']['hits']:
    print(hit['_source'])
