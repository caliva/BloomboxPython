# Bloombox Client for Python

Latest Version: `0.0.1`

This Python package provides an API client for [Bloombox](https://bloombox.io) Cloud APIs. Bloombox APIs are built and served using [gRPC](https://grpc.io) and exposed in client libraries like this one with a more fluid interface to work with.

That being said, you can always opt to use the lower level gRPC APIs, either via gRPC+protobuf (docs coming soon) or via JSON REST, using transcoding (docs coming soon on this too).


### Using the code

Published libs coming soon. In the meantime, see `Building the code`.


### Building the code

Building the code is easy and follows standard Swift packaging conventions. There is also a `Makefile` packaged with various useful routines - you'll use `make` if you are developing on the code.

**Required tools:**
- Python 2.7
- `virtualenv`
- `git`
- `make` and other CLI tools
- Code access to private schema repos for Bloombox


## Services


### Shop API

The Shop API allows interaction with ordering, user enrollment and verification, and other tools. Demo code coming soon.


### Telemetry API

The Telemetry API allows you to relay events as they happen, so they may be attributed in user flows and other Bloombox-provided metrics.


## Licensing

Copyright © 2017 Bloombox, LLC.

A copy of the Apache 2.0 license is enclosed at `LICENSE.txt`, along with additional notices in `NOTICE.txt`. Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the license.

