# Map of Events ( backend part)

A backend part of map of events.

<!-- TOC -->

* [Map of Events ( backend part)](#map-of-events--backend-part-)
    * [TODO](#todo)
    * [Usage of API](#usage-of-api)
        * [Fetch filtration data](#fetch-filtration-data)
            * [Request](#request)
            * [Response](#response)
        * [Make a filtration request](#make-a-filtration-request)
            * [Request](#request)
            * [Response](#response)
        * [Retrieve minimal info about event](#retrieve-minimal-info-about-event)
            * [Request](#request)
            * [Response](#response)
        * [Retrieve a full info about event](#retrieve-a-full-info-about-event)
            * [Request](#request)
            * [Response](#response)
    * [Deploy and Running](#deploy-and-running)

<!-- TOC -->

## TODO

- [x] Retrieve Organizer Levels

- [x] Get All Organizers
- [x] Get Organizer
- [x] Create Organizer
- [x] Delete Organizer
- [x] Update Organizer

- [x] Get All Competitors

- [x] Get All FoundingTypes

- [x] Get All founding ranges
- [x] Get Founding Range
- [x] Update Founding Range
- [x] Create Founding Range
- [x] Delete Founding Range

- [x] Get CoFounding Range
- [x] Update CoFounding Range
- [x] Create CoFounding Range
- [x] Delete CoFounding Range

- [ ] Get All Events
- [ ] Get Event
- [ ] Update Event
- [ ] Create Event
- [ ] Delete Event

- [ ] Get Subjects By Event
- [ ] Get Subject
- [ ] Update Subject
- [ ] Create Subject
- [ ] Delete Subject

- [ ] Get Precursors By Event(Precursor)
- [ ] Get Precursors By Event(Successor)
- [ ] Update Precursor
- [ ] Delete Precursor
- [ ] Create Precursor

## Usage of API

In this section the `{begin}` is a shortcut to `{server}/api/v1`
where `{server}` is an address of running application.

| what does                           | method | path                                                    | info                                       | 
|-------------------------------------|--------|---------------------------------------------------------|--------------------------------------------|
| Fetch filtration data               | `GET`  | `{begin}/filtration`                                    | [more](#fetch-filtration-data)             |
| Make filtration request             | `POST` | `{begin}/filtration`                                    | [more](#make-a-filtration-request)         |
| Retrieve a minimal info about event | `GET`  | `{begin}/event/<id>/minimal`, where `id` is ID of Event | [more](#retrieve-minimal-info-about-event) |
| Retrieving full info about event    | `GET`  | `{begin}/event/<id>`, where `id` is ID of Event         | [more](#retrieve-a-full-info-about-event)  |

### Fetch filtration data

This request will retrieve all data that is used in filtration(subjects, prices etc.).

`GET` to `{begin}/filtration`

#### Request

does not have.

#### Response

```json
{
  "founding_types": [
    "founding_type_0",
    "founding_type_1",
    "founding_type_2"
  ],
  "founding_range": {
    "low": 0,
    "high": 250000
  },
  "co_founding_range": {
    "low": 0,
    "high": 0
  },
  "submission_date": "2012-04-23T18:25:43.511Z",
  "competitor_requirements": [
    {
      "id": 0,
      "competitor": "name of competitor"
    },
    {
      "id": 1,
      "competitor": "name of competitor 1"
    }
  ],
  "subjects": [
    "subject 0",
    "subject 1",
    "subject 2",
    "subject 3"
  ]
}
```

### Make a filtration request

This request will send a set of filters to the server and will retrieve a list of IDs of Event where every event fits
this filters.

`POST` to `{begin}/filtration`

#### Request

Request contains fields that the result of [Fetch filtration data](#fetch-filtration-data) has.
But it should add only the fields, that actually used in the filtration:

```json
{
  "founding_type": "type_X",
  "founding_range": {
    "low": 1000,
    "high": 5000
  },
  "subjects": [
    "subject_A",
    "subject_B",
    "subject_C",
    "subject_D",
    "subject_E"
  ]
}
```

#### Response

List of IDs of Event where every event fits this filters.

```json
[
  5001334131,
  13132123135,
  57657564,
  453543
]
```

### Retrieve minimal info about event

Retrieves minimal information of event by it's ID.

`GET` to `{begin}/event/<id>/minimal`, where `id` is ID of Event. ID is an integer.

#### Request

does not have. The info of request is stored in the path(id).

#### Response

```json
{
  "organizer": {
    "name": "Organizer X",
    "logo": "organizer_x_logo_from_statics.png",
    "level": "organizer_level_x"
  },
  "title": "event X",
  "submission_date": "2012-04-23T18:25:43.511Z",
  "tlr": 5
}
```

### Retrieve a full info about event

Retrieving full info about event

`GET` to `{begin}/event/<id>`, where `id` is ID of Event

#### Request

does not have. The info of request is stored in the path(id).

#### Response

contains a complete set of information about this event.

```json
{
  "organizer": {
    "name": "Organizer X",
    "logo": "organizer_x_logo_from_statics.png",
    "level": "organizer_level_x"
  },
  "title": "Event Y",
  "founding_type": [
    "founding_type_1",
    "founding_type_2"
  ],
  "founding_range": {
    "low": 0,
    "high": 50000
  },
  "co_founding_range": {
    "low": 0,
    "high": 0
  },
  "submission_deadline": "2012-04-23T18:25:43.511Z",
  "consideration_period": "2012-04-23T18:25:43.511Z",
  "realisation_period": "2012-04-23T18:25:43.511Z",
  "result": "...",
  "site": "https://hello.com",
  "document": "https://hello.com/docs/event_y.pdf",
  "internal_university_contacts": "Phone Number, Name",
  "tlr": 5
}
```

### Calls for adding page.

The list of API endpoints for Panel to add new entities.

Logical way to do so:

#### Fetch the things available settings.

`{begin}/competitor` - list of available competitors returns:

```json
[
  {
    "id": 1,
    "name": "Person"
  },
  {
    "id": 2,
    "name": "University"
  }
]
```

`{begin}/organizers_level` - list of available organizer's levels:

```json
[
  {
    "id": 1,
    "name": "Federal",
    "code": "FED"
  },
  {
    "id": 2,
    "name": "Regional",
    "code": "REG"
  }
]
```

`{begin}/founding_types` - list of available founding types:

```json
[
  {
    "id": 1,
    "name": "Grant"
  },
  {
    "id": 2,
    "name": "Credit"
  }
]
```

`{begin}/organizer` - with `GET` returns list of available organizers.

```json
[
  {
    "id": 1,
    "name": "OrganizerX",
    "logo": "https://logo.example.com",
    "level": 1
  }
]
```

#### Create Organizer entity and send it to server.

`POST` to `{begin}/organizer` with JSON request:

```json
{
  "name": "",
  "logo": "",
  "level": null
}
```

#### Create Event entity and send it to server.

#### Send set of competitors type to server.

#### Send set of subjects to server.

## Deploy and Running

Currently, does not support any mechanisms of containerisation
(they will be added soon).

```bash
git clone https://github.com/sevsu-map-of-events/sevgu-event-map-backend.git

cd sevgu-event-map-backend

# will create a virtual env and install deps
pipenv install

python3 manage.py makemigrations
python3 manage.py migrate

# start the server
python3 manage.py runserver
```

