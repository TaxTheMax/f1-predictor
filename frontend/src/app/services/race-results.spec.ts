import { TestBed } from '@angular/core/testing';
import { RaceResults } from './race-results';

describe('RaceResults', () => {
  let service: RaceResults;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(RaceResults);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
