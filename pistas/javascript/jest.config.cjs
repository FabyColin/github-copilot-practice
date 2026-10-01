/**
 * Tres proyectos de Jest:
 *  - server:      pruebas de la API (src/), entorno Node
 *  - web:         pruebas de componentes React (web/), entorno jsdom
 *  - ejercicios:  validaciones de los ejercicios (solo se corren a propósito: npm run test:ej)
 */
const comun = {
  transform: { '^.+\\.[jt]sx?$': 'babel-jest' },
  moduleNameMapper: { '\\.css$': '<rootDir>/test/styleMock.cjs' },
};

module.exports = {
  projects: [
    {
      ...comun,
      displayName: 'server',
      testEnvironment: 'node',
      testMatch: ['<rootDir>/src/**/*.test.js'],
    },
    {
      ...comun,
      displayName: 'web',
      testEnvironment: 'jsdom',
      setupFilesAfterEnv: ['<rootDir>/test/setupTests.js'],
      testMatch: ['<rootDir>/web/**/*.test.{js,jsx}'],
    },
    {
      ...comun,
      displayName: 'ejercicios',
      testEnvironment: 'node',
      testMatch: ['<rootDir>/ejercicios/**/*.test.js'],
    },
  ],
};
