RUN := 'uv run --frozen'
CUTOFF := '"7 days ago"'

dev:
	{{ RUN }} pelican -lr 

generate:
	{{ RUN }} pelican 

upgrade:
	{{ RUN }} uv lock --upgrade --exclude-newer {{ CUTOFF }}
