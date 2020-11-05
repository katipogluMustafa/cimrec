# Cimrec : Recommendation Framework

> Cimrec Türkçe 'simrek' diye telafuz edilir.

Cimrec is a framework of recommendation system algorithms. This framework help you to make recommendations in any programming language using the respected API for the target langauge. 

## Why use cimrec? 

Cimrec gets your data as input, and based on your choice of algorithms and accuracy metrics, a high quality recommendation is provided.

Cimrec also provides caching like mechanisms in order to use as minimum resources as possible.


### Example Use Case

* Given a user's history of movie ratings in netflix, we provide list of movies to recommend the user.

* Given a user's list of item purchases in amazon, we provide list of products to recommend to the target user.

* Given a movie, we provide list of similar movies to recommend the users who has watched the movie.

## Current Progress

Currently, the framework is at its inital phase. This project has been started as a research on a new user-based similarity method (Timebin Based Neighbourhood) as the result of our [Temporal Drift research](https://github.com/katipogluMustafa/TemporalDrift).

Temporal Drift research was a way for us to get to know the recommendation system algoritms and create our target framework cimrec. As the temporal drift project advaced, we also tried to create a basic framework as the skeleton of cimrec. All states of this skeleton framework has been traced as [Project Alpha](https://github.com/katipogluMustafa/project-alpha/).

## Roadmap

1. Create Base Framework With TDD
2. Add User Based Collaborative Filtering Algorithms
3. Add Deep Neural Network Based Recommendation Algorithms
4. Add support for Other Data other than Netflix and Movielens
5. Provide Public API for Phyton
6. Add Other families of Recommendation and rework on roadmap.

## In Progress

We are currently at phase 1:Create Base Framework With TDD .

The aim of this phase is to create a better base for all future phases by converting the [Project Alpha](https://github.com/katipogluMustafa/project-alpha/) to more clean written test drivenly development code base.

## For Contributors

If you want to make contributions, you are expected to follow the following guidelines.

### Project Structure

Cimrec uses project uses [Package Oriented Design](https://www.ardanlabs.com/blog/2017/02/package-oriented-design.html).

[Package layout](https://medium.com/@benbjohnson/standard-package-layout-7cdbc8391fc1) follows the following guidelines as described at the article. 

* Root package is for domain types
* Group subpackages by dependency
* Use a shared mock subpackage
* Main package ties together dependencies

### Clean Code

We follow the general guidelines of the [Clean Code: A Handbook of Agile Software Craftsmanship](https://www.amazon.com.tr/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882)

In summary: 

* K & R style indentation.

* Every function should do one thing.
  * Reduce the function length as much as possible until you cant.
  * Optimum function length 4 to 10 lines.

* Other than public APIs no code should have comments.
  * Code should describe itself.
  * Every variables, class, function name should describe itself.
  * If any comment exists, it is critical to know.

* Files should be 50-100lines on average, at max 500

### Code Style

We use [pep8](https://www.python.org/dev/peps/pep-0008/) code styling standard. 
 