Steps to configure this project into your system.

1.	Install Git if you don’t have in your system from the site: 

          https://git-scm.com/download/win

2.	Open Git Bash and clone this repository in a directory using the command 

          git clone https://github.com/Nivedita01/docker_assessment.git

3. Once the project is cloned, open the cloned project in a code editor like Pycharm

4. Open terminal and activate virtual environment using the command

          .\venv\Scripts\activate
          
   Note: If there is another venv active on your workspace by default, use 'deactivate' command first and then use the above command.

5. Install requirements.txt on this virtual environment using the command

          pip install -r requirements.txt

6. Run test suite using the command 

          pytest -n 3 –html=Reports/docker.html

