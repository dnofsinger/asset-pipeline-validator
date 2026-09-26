# Asset Pipeline Validator

## Overview

A CLI tool that scans a Maya project assets/ folder and fails if anything violates rules in the pipeline.

Currently checks for a Maya Scenes folder (and character art specifically) for:

- scenes folder exists
- textures folder exists
- exports folder exists
- correct version names
- no spaces in file names

## Features

Produces PASS and FAIL output along with violations in detail for proper Maya folder structure.

Example of character folder that has proper structure:

```
Validating files in directory: D:\02_ASSETS\characters\knight_character
[PASS] - The scenes/ folder must exist.
[PASS] - textures/ folder exists
[PASS] - exports/ folder exists
[PASS] - correct version names
[PASS] - no spaces in names
```

## Prerequisites

- Must have at least Python 3.12 installed

## Installation

## Configuration

## Running the Application

To run the validator:

Run:

```C:\> python __main__.py <CHARACTER_FOLDER```

Example:

```C:\> python __main__.py .\knight_character```

## Folder Structure

## Troubleshooting

## Contributing
