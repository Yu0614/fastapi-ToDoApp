
# docker コンテナを立ち上げます。
up:
	docker-compose up -d --build
.PHONY: up

# docker コンテナを切断します。
down:
	docker-compose down
.PHONY: down

# db コンテナに bashで接続します。
dbConnect:
	docker exec -it db bash 
.PHONY: dbConnect

# fast-api コンテナに bashで接続します。
apiConnect:
	docker exec -it fast-api bash
.PHONY: apiConnect