FROM golang:alpine AS build

ENV GOPROXY=https://proxy.golang.org

WORKDIR /go/src/api
COPY . .

RUN go build main.go

FROM alpine
COPY --from=build /go/bin/api /go/bin/api
ENTRYPOINT ["go/bin/api"]