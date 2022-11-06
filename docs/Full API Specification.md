# Full API Specification of "Sevsu Event Map Backend"

## /api

### /v1

#### /events

##### /event

##### /organizer

`/api/v1/events/organizer`

Supports `GET` and `POST` requests.

###### GET

On `GET` it returns a list of available organizers:

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

###### POST

On `POST` request it adds a new organizer. Request is:

```json
{
  "name": "",
  "logo": "",
  "level": null
}
```

And it returns a new entity of organizer.

##### organizer_levels/

`/api/v1/events/organizer_levels`


Supports `GET`.

Returns a list of available organizer_levels:

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

##### competitor/

`/api/v1/events/competitor`


Supports `GET`.

Returns a list of available competitor's types:

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

##### founding_types/

`/api/v1/events/founding_types`


Supports `GET` request.

Returns a list of available founding types:

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

## /admin

Access to `admin/` opens an administration panel.
It should not be used as a general approach to insert data in the system.