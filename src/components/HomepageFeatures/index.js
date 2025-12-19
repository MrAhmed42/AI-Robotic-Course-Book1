
import React from 'react';
import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

const FeatureList = [
  {
    title: 'Spec-Driven Robotics',
    /* We will use generic icons or you can keep the svgs if you like them */
    Svg: require('@site/static/img/undraw_docusaurus_mountain.svg').default,
    description: (
      <>
        A rigorous technical curriculum focused on hardware specifications, 
        ROS 2 integration, and real-world humanoid deployment.
      </>
    ),
  },
  {
    title: 'Physical AI & VLA',
    Svg: require('@site/static/img/undraw_docusaurus_tree.svg').default,
    description: (
      <>
        Deep dives into Vision-Language-Action (VLA) models and the 
        "Robot Brain" architecture powering modern autonomous agents.
      </>
    ),
  },
  {
    title: 'Digital Twin Simulation',
    Svg: require('@site/static/img/undraw_docusaurus_react.svg').default,
    description: (
      <>
        Master Sim-to-Real strategies using high-fidelity digital twins 
        to accelerate humanoid learning and testing safety.
      </>
    ),
  },
];

function Feature({Svg, title, description}) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <Heading as="h3" className={styles.featureTitle}>{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}