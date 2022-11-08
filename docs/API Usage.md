# Usage of API

## CRUDs

| METHOD          | PATH                                   | What does                                                            |
|-----------------|----------------------------------------|----------------------------------------------------------------------|
| `GET`           | `api/v1/events/organizer_level/`       | Returns a list of available organizer levels                         |
| `GET`           | `api/v1/events/organizer/`             | Returns a list of available organizers                               |
| `POST`          | `api/v1/events/organizer/`             | Adds a new organizer to list                                         |
| `GET`           | `api/v1/events/organizer/{id}`         | Gets an organizer by it's ID                                         |
| `POST` or `PUT` | `api/v1/events/organizer/{id}`         | Updates existing organizer                                           |
| `DELETE`        | `api/v1/events/organizer/{id}`         | Deletes organizer                                                    |
| `GET`           | `api/v1/events/competitors/`           | Returns a list of available competitors                              |
| `GET`           | `api/v1/events/founding_types/`        | Returns a list of available founding types                           |
| `GET`           | `api/v1/events/founding_range/`        | Return a list of founding range                                      |
| `POST`          | `api/v1/events/founding_range`         | Creates a new founding range                                         |
| `GET`           | `api/v1/events/founding_range/{id}`    | Returns a founding range with given ID                               |
| `POST` or `PUT` | `api/v1/events/founding_range/{id}`    | Updates existing founding range                                      |
| `DELETE`        | `api/v1/events/founding_range/{id}`    | Deletes existing range                                               |
| `GET`           | `api/v1/events/co_founding_range/`     | Returns a list of co-founding ranges                                 |
| `POST`          | `api/v1/events/co_founding_range/`     | Creates a new co-founding range                                      |
| `GET`           | `api/v1/events/co_founding_range/{id}` | Returns a co-founding range with given ID                            |
| `POST` or `PUT` | `api/v1/events/co_founding_range/{id}` | Updates existing co-founding range                                   |
| `DELETE`        | `api/v1/events/co_founding_range/{id}` | Deletes existing range                                               |
| `GET`           | `api/v1/events/event`                  | Returns a list of events                                             |
| `POST`          | `api/v1/events/event`                  | Creates a new event                                                  |
| `GET`           | `api/v1/events/event/{id}`             | Returns event with given ID                                          |
| `POST` or `PUT` | `api/v1/events/event/{id}`             | Updates the even with given ID                                       |
| `DELETE`        | `api/v1/events/event/{id}`             | Destroys event with given ID                                         |
| `GET`           | `api/v1/events/event/{id}/minimal`     | Returns minimal info about event                                     |
| `GET`           | `api/v1/events/subject/`               | Returns a list of subjects                                           |
| `GET`           | `api/v1/events/subject/event/{id}`     | Returns a list of subjects for which field "event" is equal given id |
| `GET`           | `api/v1/events/subject/id/{id}`        | Returns subject with given id                                        |
| `POST` or `PUT` | `api/v1/events/subject/id/{id}`        | Updates subject with given id                                        |
| `DELETE`        | `api/v1/events/subject/id/{id}`        | Deletes subject with given id                                        |
