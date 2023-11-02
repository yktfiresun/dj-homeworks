import pytest
from rest_framework.test import APIClient
from model_bakery import baker
from students.models import Student,Course

@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory

@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        courses_set = baker.make(Course,*args, **kwargs)
        return courses_set
    return factory

@pytest.mark.django_db
def test_get_firstcourse(client, course_factory,student_factory):
    students = student_factory(_quantity=5)
    courses = course_factory(_quantity=10)
    for course in courses:
        course.students.set(students)

    response = client.get('/api/v1/courses/1/')
    assert response.status_code == 200
    data = response.json()
    assert data['id'] == 1

@pytest.mark.django_db
def test_get_courses(client, course_factory, student_factory):
    students = student_factory(_quantity=5)
    courses = course_factory(_quantity=10)
    for course in courses:
        course.students.set(students)
    response = client.get('/api/v1/courses/')
    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(courses)

@pytest.mark.django_db
def test_get_course_by_id(client, course_factory, student_factory):
    students = student_factory(_quantity=5)
    courses = course_factory(_quantity=10)
    for course in courses:
        course.students.set(students)
    response = client.get('/api/v1/courses/', data={'id': courses[0].id })
    assert response.status_code == 200
    data = response.json()
    assert data[0]['id'] == courses[0].id

@pytest.mark.django_db
def test_get_course_by_name(client, course_factory, student_factory):
    students = student_factory(_quantity=5)
    courses = course_factory(_quantity=10)
    for course in courses:
        course.students.set(students)
    response = client.get('/api/v1/courses/', data={'name': courses[0].name })
    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == courses[0].name

@pytest.mark.django_db
def test_create_course(client):
    count = Course.objects.count()
    response = client.post('/api/v1/courses/', data={'name': 'CourseName1'})

    assert response.status_code == 201
    assert Course.objects.count() == count + 1

@pytest.mark.django_db
def test_update_course(client,student_factory,course_factory):
    students = student_factory(_quantity=5)
    courses = course_factory(_quantity=10)
    for course in courses:
        course.students.set(students)

    response = client.patch('/api/v1/courses/{}/'.format(courses[0].id), data={'name': 'courseName2', })

    assert response.status_code == 200

@pytest.mark.django_db
def test_delete_course(client,student_factory,course_factory):
    students = student_factory(_quantity=5)
    courses = course_factory(_quantity=10)
    for course in courses:
        course.students.set(students)

    response = client.delete('/api/v1/courses/{}/'.format(courses[0].id))

    assert response.status_code == 204

