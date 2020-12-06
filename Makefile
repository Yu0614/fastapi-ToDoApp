
# docker コンテナを立ち上げます。
up:
	docker-compose up -d --build
.PHONY: up

# docker コンテナを切断します。
down:
	docker-compose down
.PHONY: down

# db コンテナに bashで接続します。
db:
	docker exec -it db bash 
.PHONY: db

# fast-api コンテナに bashで接続します。
api:
	docker exec -it fast-api bash
.PHONY: api

# コンテナを再起動します。
restart:
	make down && make up
.PHONY: restart