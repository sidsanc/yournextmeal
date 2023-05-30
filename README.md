# Your Next Meal

![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?style=flat&logo=github)
[![Python](https://img.shields.io/badge/Code-Python-informational?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Code-Django-092E20?style=flat&logo=django&logoColor=white)](https://www.djangoproject.com/start/)
[![React](https://img.shields.io/badge/Code-React-informational?style=flat&logo=react&color=61DAFB)](https://react.dev/)
[![MongoDB](https://img.shields.io/badge/DataBase-MongoDB-4EA94B?style=flat&logo=mongodb&logoColor=white)](https://www.mongodb.com/)
![AWS](https://img.shields.io/badge/AWS-Amazon%20Web%20Services-orange?style=flat&logo=amazon-aws)
![Jenkins](https://img.shields.io/badge/CI-Jenkins-red?style=flat&logo=jenkins)

Your Next Meal is a donor-receiver match platform developed using Django, ReactJS, and MongoDB. The project aims to connect food donors with organizations or individuals in need, reducing food waste and ensuring that no one goes hungry.

## Features

- **Donor-Receiver Match**: The platform allows food donors to register and provide details about the surplus food they want to donate. Receivers can sign up and specify their requirements.
- **Efficient Data Storage**: AWS services such as Lambda functions and S3 are utilized for efficient data storage and retrieval, ensuring scalability and reliability.
- **Deployment and Development**: The project achieved 95% uptime and minimized data loss by leveraging efficient deployment strategies with GitHub and Jenkins. Development time was reduced by 30% through streamlined processes.

## Tech Stack

- **Backend**: Django, Python

- **Frontend**: ReactJS, JavaScript, HTML, CSS

- **Database**: MongoDB

- **Cloud Services**: AWS (Lambda, S3)

- **Version Control**: Git, GitHub

- **CI/CD**: Jenkins

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/your-next-meal.git
   ```

2. Navigate to the project directory:

   ```bash
   cd your-next-meal
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the development server:

   ```bash
   python manage.py runserver
   ```

5. Open your web browser and access the application at `http://localhost:8000`.

## Contributing

Contributions are welcome! If you would like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create your feature branch: `git checkout -b feature/my-feature`.
3. Commit your changes: `git commit -am 'Add my feature'`.
4. Push to the branch: `git push origin feature/my-feature`.
5. Open a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any inquiries or suggestions, feel free to reach out to me:

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/siddhant-sancheti)
[![Email](https://img.shields.io/badge/Email-Contact-red?style=flat&logo=gmail&logoColor=white)](mailto:sanchetisiddhantk@gmail.com)

Let's connect and make a difference together!
Install python 3.8, pip3

Checkout repo: 
https://github.com/sidsanc/yournextmeal


Set Up venv

python3 -m venv ./
source ./bin/activate


pip3 install -r requirements.txt


If you are getting 
[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate 
try: 
open /Applications/Python <local version>/Install\ Certificates.command



To run application locally:
python3  manage.py runserver
