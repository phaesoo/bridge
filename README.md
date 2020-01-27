# Relay
Backend project for various kinds of inter-server communication


## Prerequisites

- Redis: message queue for socketio, database


## Debugging/Testing

Run debug server

```console
$ bash relay/run_debug.sh
```

Unit test

```console
$ bash relay/run_test.sh
```


## Tech stacks

Framework: Flask
Communication: socketio, HTTP(REST API)
Database: Redis


## Infra

Database: Redis


## Todo list

Main workflow:

- [x] Basic communication test with both socket.io and REST API.
- [ ] Database connection for temporal/mid to long term data storing.
- [ ]

Advanced:

- [ ] Documentation
- [ ] Logging
- [ ] Unit testing
- [ ] Exceptional handling