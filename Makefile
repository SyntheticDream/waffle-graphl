all: frontend

frontend: backend/static/index.html
	mkdir -p backend/static
	cd frontend && npm run build && cp -r ../frontend/dist/* ../backend/static/
