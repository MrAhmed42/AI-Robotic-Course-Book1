# Implementation Plan: AI/Spec-Driven Robotics Book (Hackathon Edition)

**Branch**: `1-robotics-book-spec`
**Date**: 2025-12-06
**Input Spec**: `/specs/1-robotics-book-spec/spec.md`
**Goal**: Deliver a fully functional, static technical book website within the hackathon timeline.

---

## Summary

This plan implements a static, AI/Spec-Driven technical book on Physical AI & Humanoid Robotics using Docusaurus and GitHub Pages.
The focus is on high-quality content, clean structure, fast delivery, and zero backend risk.

Phase 1 Scope (Book Only) excludes RAG, backend, authentication, personalization, and translation.

---

## Technical Context

- Language: Markdown + React (via Docusaurus)
- Framework: Docusaurus v3
- Hosting: GitHub Pages
- AI Usage: Claude Code for spec → content generation
- Testing: Manual content validation
- Target Platform: Web (Static)

 ---

## Scope (Hackathon Only)

### Included
- Docusaurus Project Setup
- Sidebar and Navigation
- Four Core Modules:
  1. ROS 2 Fundamentals
  2. Digital Twins (Gazebo + Unity)
  3. AI Robot Brain (NVIDIA Isaac)
  4. Vision-Language-Action (VLA)
- Capstone Project: Autonomous Humanoid
- Clean UI and Mobile Responsive Design
- GitHub Pages Deployment

### Excluded
- No Backend
- No RAG Chatbot
- No Login / Authentication
- No Database
- No Personalization
- No Urdu Translation

---

## Content Rules

- English is the primary source of truth
- Each chapter follows this structure:
  - Concept
  - Architecture
  - Implementation
- Beginner to Intermediate level
- Practical and implementation-focused

---

## Project Structure

```text
/
├── docs/
│   ├── module-1-ros2/
│   ├── module-2-digital-twins/
│   ├── module-3-ai-brain/
│   ├── module-4-vla/
│   └── capstone/
├── sidebars.js
├── docusaurus.config.js
└── README.md
```