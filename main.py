from piccolo.table import Table
from piccolo.columns import Serial, Varchar, ForeignKey, Integer, Timestamp, Interval, Numeric, UUID, JSON, Boolean
from fastapi import FastAPI
import uvicorn
from fastapi.routing import Mount
from piccolo_api.crud.endpoints import PiccoloCRUD
from piccolo_admin.endpoints import create_admin

class Manager(Table):
    id = Serial(primary_key=True)
    name = Varchar()


class Band(Table):
    id = Serial(primary_key=True)
    name = Varchar()
    manager = ForeignKey(references=Manager)
    popularity = Integer()


class Venue(Table):
    id = Serial(primary_key=True)
    name = Varchar()
    capacity = Integer()


class Concert(Table):
    id = Serial(primary_key=True)
    band_1 = ForeignKey(references=Band)
    band_2 = ForeignKey(references=Band)
    venue = ForeignKey(references=Venue)
    starts = Timestamp()
    duration = Interval()


class Ticket(Table):
    id = Serial(primary_key=True)
    concert = ForeignKey(references=Concert)
    price = Numeric()

class DiscountCode(Table):
    id = Serial(primary_key=True)
    code = UUID()
    active = Boolean()


class RecordingStudio(Table):
    id = Serial(primary_key=True)
    name = Varchar()
    facilities = JSON()


app = FastAPI(
    routes=[
        Mount(
            "/",
            create_admin(
                tables=[Manager,Ticket,Band,Concert,Venue,RecordingStudio,DiscountCode],
                site_name="Piccolo PlayGround Admin",
                # Required when running under HTTPS:
                # allowed_hosts=['my_site.com']
            ),
        ),
    ],
)



if __name__ == '__main__':
    uvicorn.run(app)

