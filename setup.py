from setuptools import setup, find_packages

setup(
   name='EasyGPTpy',             # Name of your package
   version='0.1.0',              # Version of your package
   packages=find_packages(),     # Automatically find packages in the project
   install_requires=[            # List of dependencies
       # 'somePackage',
   ],
   author='Your Name',
   author_email='your.email@example.com',
   description='A short description of your package',
   long_description=open('README.md').read(),
   long_description_content_type='text/markdown',
   url='https://github.com/yourusername/EasyGPTpy',  # Replace with your package's GitHub repo URL
   classifiers=[
       'Programming Language :: Python :: 3',
       'License :: OSI Approved :: MIT License',
       'Operating System :: OS Independent',
   ],
   python_requires='>=3.6',
)
