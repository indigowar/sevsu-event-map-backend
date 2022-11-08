# Usage of API

## CRUDs

| METHOD          | PATH                                   | What does                                                            |
|-----------------|----------------------------------------|----------------------------------------------------------------------|
| `GET`           | `api/events/v1/organizer_level/`       | Returns a list of available organizer levels                         |
| `GET`           | `api/events/v1/organizer/`             | Returns a list of available organizers                               |
| `POST`          | `api/events/v1/organizer/`             | Adds a new organizer to list                                         |
| `GET`           | `api/events/v1/organizer/{id}`         | Gets an organizer by it's ID                                         |
| `POST` or `PUT` | `api/events/v1/organizer/{id}`         | Updates existing organizer                                           |
| `DELETE`        | `api/events/v1/organizer/{id}`         | Deletes organizer                                                    |
| `GET`           | `api/events/v1/competitors/`           | Returns a list of available competitors                              |
| `GET`           | `api/events/v1/founding_types/`        | Returns a list of available founding types                           |
| `GET`           | `api/events/v1/founding_range/`        | Return a list of founding range                                      |
| `POST`          | `api/events/v1/founding_range`         | Creates a new founding range                                         |
| `GET`           | `api/events/v1/founding_range/{id}`    | Returns a founding range with given ID                               |
| `POST` or `PUT` | `api/events/v1/founding_range/{id}`    | Updates existing founding range                                      |
| `DELETE`        | `api/events/v1/founding_range/{id}`    | Deletes existing range                                               |
| `GET`           | `api/events/v1/co_founding_range/`     | Returns a list of co-founding ranges                                 |
| `POST`          | `api/events/v1/co_founding_range/`     | Creates a new co-founding range                                      |
| `GET`           | `api/events/v1/co_founding_range/{id}` | Returns a co-founding range with given ID                            |
| `POST` or `PUT` | `api/events/v1/co_founding_range/{id}` | Updates existing co-founding range                                   |
| `DELETE`        | `api/events/v1/co_founding_range/{id}` | Deletes existing range                                               |
| `GET`           | `api/events/v1/event`                  | Returns a list of events                                             |
| `POST`          | `api/events/v1/event`                  | Creates a new event                                                  |
| `GET`           | `api/events/v1/event/{id}`             | Returns event with given ID                                          |
| `POST` or `PUT` | `api/events/v1/event/{id}`             | Updates the even with given ID                                       |
| `DELETE`        | `api/events/v1/event/{id}`             | Destroys event with given ID                                         |
| `GET`           | `api/events/v1/event/{id}/minimal`     | Returns minimal info about event                                     |
| `GET`           | `api/events/v1/subject/`               | Returns a list of subjects                                           |
| `GET`           | `api/events/v1/subject/event/{id}`     | Returns a list of subjects for which field "event" is equal given id |
| `GET`           | `api/events/v1/subject/id/{id}`        | Returns subject with given id                                        |
| `POST` or `PUT` | `api/events/v1/subject/id/{id}`        | Updates subject with given id                                        |
| `DELETE`        | `api/events/v1/subject/id/{id}`        | Deletes subject with given id                                        |
