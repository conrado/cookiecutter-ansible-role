import os

# make local testing the default testing
os.symlink(
  './local',
  'molecule/default')

# let github configuration for converge and verify match local configuration
os.symlink(
  '../local/converge.yml',
  'molecule/github/converge.yml')
os.symlink(
  '../local/verify.yml',
  'molecule/github/verify.yml')
