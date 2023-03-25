# Learning Analytics Visualisation

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## About The Project

This project aims to glean insights from publicly available parking data from events in Melbourne, including:

- User management functionality
- Embedded Microsoft Power BI visualisation dashboard

The live application can be viewed at [https://lav-app.herokuapp.com/](https://lav-app.herokuapp.com/).

### Built With

This section should list any major frameworks. Delete this line once we settle on framework(s).

- [Bootstrap](https://getbootstrap.com)
- [Django](https://www.djangoproject.com/)
- [Microsoft Power BI](https://powerbi.microsoft.com/en-us/)

## Getting Started

To get started in your local environment, ensure that the prerequisites are met and then
follow the installation instructions.

### Prerequisites

You will need to follow installations steps at the relevant site to ensure the listed apps are set up on local machine, if not installation step below may not work.

- [Docker](https://www.docker.com/)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/mark-rmit/learning-analytics-visualisation.git
   cd learning-analytics-visualisation
   ```

2. Create .env
   ```sh
   cp lav/.env.example lav/.env
   ```

3. Once `lav/.env` has been created, update its `SECRET_KEY` to something secure. Then update 
   `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `EMAIL_HOST`, `DEFAULT_FROM_EMAIL` and `EMAIL_PORT` as
   appropriate. Any SMTP account will do, and you can create a free email account at gmail.com.

4. Start the development server with Docker:
   ```
   docker-compose up
   ```

5. Open another terminal in your project folder and run migrations:
   ```
   docker-compose run web python manage.py migrate
   ```

6. Point your web browser to `http://localhost:8000`. You should see the application homepage.

### Running Tests

To run tests, execute the following commands.

```
docker-compose run web python manage.py collectstatic --noinput
docker-compose run web python manage.py test
```

## Roadmap

See our [Trello Board](https://trello.com/b/9Ab0Yg6K) for a list of proposed features.

## Contributing

Contributions must adhere to the following process:

1. Create your Feature Branch off the Development Branch (`git checkout -b feature/amazing-feature develop`)
2. Commit your Changes (`git commit -m 'Add some amazing features'`)
3. Push to the Branch (`git push origin feature/amazing-feature`)
4. Open a Pull Request to merge into the `develop`

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Mark Harris - s3427191@student.rmit.edu.au

Project Link: [https://github.com/mark-rmit/learning-analytics-visualisation](https://github.com/mark-rmit/learning-analytics-visualisation)

## Acknowledgements and References

- [Gitignore starter template for Django - DjangoWaves, 2021](https://djangowaves.com/tips-tricks/gitignore-for-a-django-project/)
