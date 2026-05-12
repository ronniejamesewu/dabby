# Dabby UI Principles

## Purpose

This document defines the structural UI rules for the Dabby Session Log system. It is a source of truth for layout hierarchy, component roles, and interaction boundaries. It exists to prevent design drift between conversation and implementation in `Dabby_Log_Generator.py`.

---

## 1. UI Hierarchy (Top-Level Structure)

The application is organized into three layers:

### 1. Header (Identity Layer)

* Displays only:

  * Primary title: **Session Log**
  * Subtitle: **Dabby the House Rig**
* No additional descriptive text
* No links or interactive elements
* No visual framing that competes with content below
* Function: identity only

---

### 2. Dashboard (Observability Layer)

* Displays computed system statistics derived from `COMPLETED_RUNS`
* Must be **read-only**
* No clickable elements
* No navigation role
* Function: reflect system state, not enable action

Examples of allowed content:

* aggregate session counts
* temperature averages
* strain usage distribution

Non-goals:

* no strain selection
* no navigation links
* no interactive filtering controls

---

### 3. Strain Browser (Action Layer)

* Primary interaction surface
* Used for:

  * selecting strains
  * reviewing last run
  * viewing “What to Try Next”
* Contains search + scrollable list
* Each row represents a navigable strain context

This is the **only primary navigation system** in the UI.

---

## 2. Component Roles

### Header

* Identity only
* No interaction
* Minimal vertical footprint

### Dashboard

* Passive system telemetry
* Visual summary of global state
* No clicks, no routing

### Strain Browser

* Active decision surface
* Supports navigation and exploration
* Contains all user intent pathways

---

## 3. Hierarchy Rules

* Dashboard must never visually dominate Strain Browser
* Strain Browser is the primary working interface
* Header must never resemble a landing page hero section

Order of importance:

1. Strain Browser (action)
2. Dashboard (state)
3. Header (identity)

---

## 4. Interaction Rules

* Only Strain Browser contains navigation links
* Dashboard must not contain clickable UI elements
* Header must not contain any interaction

---

## 5. Visual Weight Guidelines

* Header: lowest visual weight
* Dashboard: medium visual weight (but passive)
* Strain Browser: highest visual weight

Visual emphasis must align with user intent, not data volume.

---

## 6. Design Philosophy

This system prioritizes:

* low friction mobile usage
* fast strain recall and logging
* separation of state (dashboard) from action (browser)
* minimal cognitive overhead in navigation

The interface is not a dashboard app. It is a session log with a navigation surface.
