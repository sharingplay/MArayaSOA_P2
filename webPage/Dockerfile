# Stage 1

FROM node:14-alpine as build-step

RUN mkdir -p /app

WORKDIR /app

RUN npm i -g @angular/cli

COPY package.json /app

RUN npm install

COPY . /app

RUN ng config -g cli.warnings.versionMismatch false

COPY src ./src

RUN ng build 


# Stage 2

FROM nginx:1.17.1-alpine

COPY --from=build-step /app/dist/demo /usr/share/nginx/html
