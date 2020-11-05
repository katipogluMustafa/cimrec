# Cimrec : Recommendation Framework

> Cimrec Türkçe 'simrek' diye telafuz edilir.

Cimrec is a framework of recommendation system algorithms. This framework help you to make recommendation in any programming language using the respected API for the target langauge. 

## Why use cimrec? 

Cimrec gets your data as input, and based on your choice of algorithm and accuracy metrics, a high quality recommendation is provided.

Cimrec also provides caching like mechanisms in order to use as minimum resources as possible.

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

 