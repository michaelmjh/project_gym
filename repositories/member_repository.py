from db.run_sql import run_sql
from models.booking import Booking
from models.fitness_class import FitnessClass
from models.member import Member

def save(member):
    sql = "INSERT INTO members (member_name) VALUES (?) RETURNING member_id"
    values = [member.member_name]
    results = run_sql(sql, values)
    member.member_id = results[0]['member_id']
    return member

def select_all():
    members = []

    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        member = Member(row['member_name'], row['member_id'])
        members.append(member)
    return members

def select(id):
    member = None
    sql = "SELECT * FROM members WHERE member_id = ?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        member = Member(result['member_name'], result['member_id'] )
    return member

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM members WHERE member_id = ?"
    values = [id]
    run_sql(sql, values)

def update(member):
    sql = "UPDATE members SET (member_name) = (?) WHERE member_id = ?"
    values = [member.member_name, member.member_id]
    run_sql(sql, values)