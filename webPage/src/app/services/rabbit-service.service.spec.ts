import { TestBed } from '@angular/core/testing';

import { RabbitServiceService } from './rabbit-service.service';

describe('RabbitServiceService', () => {
  let service: RabbitServiceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(RabbitServiceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
